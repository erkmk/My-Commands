***********Rough File***************

.with_entities(Product.status)

print("good_file.id", good_file.id, " and ", good_file1.version)



##for CSV
with open(file.path, "r") as fp:
            count = 0
            for _ in fp:
                count += 1
                
##for Excel
wb = load_workbook(file.path)
sheet = wb.worksheets[0]
row_count = sheet.max_row
column_count = sheet.max_column

#New tests for the active/draft/pending records   
    def test_master_upload_editing(self):
        """
        -Pending records are withdrawn/updated/submitted.
        -Draft records are updated/submitted.
        -Active records are draft/updated/submitted.
        """
        file = File.query.filter_by(
            id=self.test_files["csv"]["product_good.csv"]["file_id"]
        ).one()
        parser = ProductFileParser(file, file.client_id)
        parser.validate()

        existing_records = (
                Product.query.filter_by(client_id=file.client_id)
                .with_entities(Product.id, Product.sb_id, Product.status,
                Product.client_id, Product.ndc11).all()
            )

        file = File.query.filter_by(
            id=self.test_files["csv"]["product_good.csv"]["file_id"]
        ).one()
        parser = ProductFileParser(file, file.client_id)
        parser.validate()

        # # Error on line 1 - column ndc11
        # validations = FileValidation.query.filter_by(
        #     file_id=file.id,
        #     version=file.version,
        #     level=FileValidationResultLevel.ERROR
        # )
        self.assertEqual(validations.count(), 1)
        
        
####
filtered_model = (
        model.query.filter_by(client_id=client_id, status="ACTIVE"))
filtered_model = model.query.filter_by(model.client_id==client_id,
        sqlalchemy.not_(model.status.contains('SUPERCEDED')))
        

elif same_as_existing >= len(line):
                    actions.append(
                        {
                            "file_id": self.file_rec.id,
                            "kind": FileValidationType.FIELD,
                            "level": FileValidationResultLevel.WARNING,
                            "message": "Record was exist with same value!",
                            "row": lineno + 1,
                            "column": "action",
                            "version": self.file_rec.version,
                        }
                    )
                    
                    
#############
 def record_updates(self, index, existing, updated):
        """
        Compare existing to updated records and persist any changes discovered
        to the FileValidation table.
        """
        updates = []
        same_as_existing = 0
        for column, value in updated.items():
            if (
                column in existing
                and str(existing[column]).strip().lower() != str(value).strip().lower()
            ):
                existing_value = (
                    bool2str(existing[column])
                    if isinstance(existing[column], bool)
                    else existing[column]
                )
                # To handle(violates not-null-constraint) if existing value is None.
                if not existing_value:
                    existing_value = ""

                updates.append(
                    {
                        "file_id": self.file_rec.id,
                        "kind": FileValidationType.FIELD,
                        "level": FileValidationResultLevel.CURRENT,
                        "message": existing_value,
                        "row": index,
                        "column": column,
                        "version": self.file_rec.version,
                    }
                )
            elif same_as_existing >= 45:
                updates.append(
                    {
                        "file_id": self.file_rec.id,
                        "kind": FileValidationType.FIELD,
                        "level": FileValidationResultLevel.WARNING,
                        "message": "Record was exist with same value!",
                        "row": index,
                        "column": "action",
                        "version": self.file_rec.version,
                    }
                )
            else:
                same_as_existing += 1

        return updates

filtered_model = (
        model.query.filter(model.client_id == client_id, or_(model.status == v for v in ('PENDING', 'DRAFT', 'ACTIVE')))
        )
        
filtered_model = (
        model.query.filter_by(client_id=client_id, status="ACTIVE")
        )
        
        
json.dumps([{"id": approval.id}])

sqlite3.InterfaceError: Error binding parameter 5 - probably unsupported type.

# approve the pending record(Call api to approve)
        approval = Approval.query.filter_by(
            client_id=file.client_id,
            sb_id=sb_id
        ).one()
        print("approval", approval.sb_id)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = self.client.post(
            "/common/approvals/",
            data=json.dumps([{"id": approval.id}]),
            headers=headers
        )
        self.assertEqual(response.status_code, 201)
        
####
self.assertTrue(
            validation.message.endswith("already exists and will be skipped.")
        )
        
        self.assertEqual(Product.query.count(), product_count+1)
        
gross_sales = fields.Decimal(required=True)
discount = fields.Decimal(required=True)
contract_num = fields.Str(required=True)
###Alembic 
f4458ab97d06
3182c2089d53

DirectSale.ContractNumber = Contract.ID

Here's my status:
- added three column (gross_sale, discount, contract_num) into DirectSale table.
- written down the code for non-bonafied amount calculation for direct_sale
- Now adding drop down at UI side for the same.(after adding this will go for test)
- not able to figure out where i can write the calculation for bonafied amount
- I need some clarification from your side for uploading direct_sale data that you have given.
- also need understanding of these calculation part from the basic. 

price_type_records = GPPriceType.query.filter(
            GPPriceType.client_id == g.client.id,
            GPPriceType.sb_id == price_type_id,
            GPPriceType.status.in_(("ACTIVE", "DRAFT", "PENDING")),
        ).all()
        


                
               if "gp.contract" in table_values:
                wac_amount = source_type.net_amount * func.coalesce(
                    GPContract.non_bonafide_perc, 1
                )
            else:
                wac_amount = source_type.net_amount.label("net_amount")
                

            dollar_columns.append(wac_amount)


# error = valid_decimal_precision(data["net_amount"], 12, 2)
        # if error:
        #     raise ValidationError({"net_amount": [error]})
INFO  [alembic.runtime.migration] Running stamp_revision  -> 3182c2089d53


I know you’re busy, but it would help me to have more regular check-ins with you. That way, I can guarantee that I’m on the right track. 
I’ll better understand what you look for in projects, get over the learning curve, and then be able to run on my own.
Thank you for making it a priority to highlight my work. I spent a great deal of time to get better understanding of domain (GP) and also learned all the new 
tech stack that I haven't worked on before, and it meant so much to me that you recognized my efforts on slack.
