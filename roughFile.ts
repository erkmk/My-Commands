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


approval: null
approved_by: 63
approved_on: "2020-09-03 20:46:45.067972"
approving_user: {id: 63, name: "Nick O'Brien"}
buckets_and_formulas: (43) [{…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}]
client_id: 7
date_cbk: "period_date"
date_ds: "period_date"
date_reb: "period_date"
date_tri: "period_date"
errors: []
id: 492
modified_by: 63
modified_on: "2020-09-03 20:46:45.068017 UTC"
modified_on_tmz: "2020-09-03 16:46"
modifying_user: {id: 63, name: "Nick O'Brien"}
name: "nfamp"
ordering: 5
ppd_column: "tppd"
price_type: "NFAMP"
redo_count: 0
report_template: {id: 415, modified_on: '2020-09-03 18:42:30.627024', price_type_id: 492, filepath: '/usr/src/app/upload/c27c795f-12bd-4320-b9f8-819861847ed9.xlsm', filename: 'Dermira nfamp Report Template.xlsm', …}
run_price_type:
attachments: [{…}]
effective_date: null
enabled: true
end_month: "9"
end_period: "2019-09-30"
end_year: "2019"
executing: false
id: 7748
last_started: "2021-09-02T19:48:22.878633"
ndc9_filter: ""
notes: []
output_state: "CURRENT_UNREAD"
overrides: []
price_type: {id: 492, modified_on: '2020-09-03 20:46:45.068017 UTC', errors: Array(0), price_type: 'NFAMP', sb_id: 44, …}
price_type_id: 492
run_id: 1536
stage: "ANALYSIS"
start_month: "10"
start_period: "2016-10-01"
start_year: "2016"
[[Prototype]]: Object
sb_id: 44
status: "ACTIVE"
undo_count: 1
version: 4
