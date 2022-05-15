class ProductExportView(ClientAccessView):
    max_chunk = 50
    chunk_size = 25000

    @permission(ResourceTagEnum.MD_VIEW_PRODUCT)
    def post(self):
        self.columns = product_file_format

        query = Product.query.filter_by(client_id=g.client.id, status="ACTIVE") 
        self.res = query.with_entities(Product, *product_file_format)

        temp_path = os.path.join(current_app.config["UPLOAD_FOLDER"], generate_uuid())
        with open(temp_path, "w", newline="") as out:
            self.writer = csv.writer(out, dialect="excel", quoting=csv.QUOTE_NONNUMERIC)

            self.chunk = 1
            self.export_result()

        file_remover = FileRemover()
        resp = send_file(temp_path, mimetype="text/csv", cache_timeout=0)
        file_remover.cleanup_once_done(resp, temp_path)

        return resp

    def export_result(self):
        self.writer.writerow([column for column in self.columns])

        with db.engine.connect() as conn:
            export_results = conn.execution_options(stream_results=True).execute(
                self.res.with_labels().statement
            )
            while True:
                chunked_export = export_results.fetchmany(self.chunk_size)

                if not chunked_export:
                    break

                for row in chunked_export:
                    self.writer.writerow(
                        [row[column] for column in self.columns]
                    )

                if self.chunk >= self.max_chunk:
                    break

                self.chunk += 1
