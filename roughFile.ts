*************roughFile***********


//Get tables from backend for specific clients
        this.dictService.getTables().subscribe(tables => {
            this.tables = tables;
            for (let table of this.tables) {
                if (table.value == 'md.product') {
                    this.dataTypeID = table.id
                    break
                }
            }
        });
		
		


 public getProductDataForDownload(dataTypeID, params) {
        return this.http
            .post(`/common/products/${dataTypeID}/export/`, params, { responseType: "blob" as "json" })
            .map(res => {
                return res;
            });
    }
	
###### //tooltip: app/md/components/upload/upload-detail/upload-detail.ts
tooltip: params => {
                    if(params.data == null)
                        return "";

                    let validationResults = this.getValidationResults(
                        params.data.line_number,
                        "action"
                    );
                    if (validationResults.length > 0) {
                        let response = ``;
                        validationResults.forEach(result => {
                            response += `${result.level}: ${result.message}\n`;
                        });
                        return response;
                    }
                },
##################################

valueGetter: (params) => params.data.modifying_user.name

public onGridReady(params){
        this.columnDefs =[
            {headerName: "Version", field: "version", sort: "asc"},
            {headerName: "Modified By",
            valueGetter: params => {
                let value = params.data.modifying_user;
                if (value === null) return "System";
                return value.name;
            }},
            {headerName: "Modified On", field: "modified_on"},
            {headerName: "Approved By",
            valueGetter: params => {
                let value = params.data.approving_user;
                if (value === null) return "System";
                return value.name;
            }},
            {headerName: "Approved On", field: "approved_on"},
            {headerName: "Changes", 
            cellRendererFramework: TemplateRendererComponent,
            cellRendererParams: {
                ngTemplate: this.editStatusTemplate,
            },
            }
            
        ];
		
background
Gov Pricing
we load files to s3 bucket
then icyte picks it up
and loads the file to gp
where and what are based on how the file is named