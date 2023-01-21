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


sqlalchemy.exc.IntegrityError: (psycopg2.errors.ForeignKeyViolation) update or delete on table "file" violates foreign key constraint "file_validation_file_id_fkey" on table "file_validation"

DETAIL:  Key (id)=(70050) is still referenced from table "file_validation".


[SQL: DELETE FROM md.file WHERE md.file.id IN (%(id_1)s, %(id_2)s, %(id_3)s, %(id_4)s)]

[parameters: {'id_1': 70050, 'id_2': 70051, 'id_3': 70052, 'id_4': 70053}]

        # count = FileTemplate.query.filter_by(name=line["value"]).count()
        
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.InsufficientPrivilege) permission denied for table undo_action
[SQL: DELETE FROM undo_action WHERE undo_action.object_type = %(object_type_1)s AND undo_action.stack_id = %(stack_id_1)s AND undo_action.active = false]
[parameters: {'object_type_1': 'price_type', 'stack_id_1': 3394}]


2022-07-04T14:37:44.521+05:30 sqlalchemy.exc.ProgrammingError: (psycopg2.errors.InsufficientPrivilege) permission denied for table undo_action

2022-07-04T14:37:44.521+05:30 [SQL: DELETE FROM undo_action WHERE undo_action.object_type = %(object_type_1)s AND undo_action.stack_id = %(stack_id_1)s AND undo_action.active = false]

"caniuse-lite": {
          "version": "1.0.30001035",
          "resolved": "https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001035.tgz",
          "integrity": "sha512-C1ZxgkuA4/bUEdMbU5WrGY4+UhMFFiXrgNAfxiMIqWgFTWfv/xsZCS2xEHT2LMq7xAZfuAnu6mcqyDl0ZR6wLQ=="
        },
		
		
		regression tickets GP-927,GP-928, GP-929, GP-930 
		
		
		effective_date: ""
endRow: 100
filterModel: {Name: {condition1: {type: "startsWith", filter: "nc", filterType: "text"},…}}
Name: {condition1: {type: "startsWith", filter: "nc", filterType: "text"},…}
condition1: {type: "startsWith", filter: "nc", filterType: "text"}
filter: "nc"
filterType: "text"
type: "startsWith"
condition2: {type: "endsWith", filter: "inc", filterType: "text"}
operator: "AND"
sortModel: []
startRow: 0



column_name..... customer.name
column_op....... {'type': 'startsWith', 'filter': 'nc', 'filterType': 'text', 'relation_col': 'name'}
/usr/src/app/app/common/aggrid.py:46 - apply_filters(): Filter type 'startsWith' is not implemented for relationships!


filter_clause (lower(CAST(lower(CAST(gp.customer.name AS VARCHAR)) AS VARCHAR)) LIKE :lower_1 || '%') AND (lower(CAST(lower(CAST(gp.customer.name AS VARCHAR)) AS VARCHAR)) LIKE '%' || :lower_2)

filter_clause (lower(CAST(lower(CAST(gp.customer.name AS VARCHAR)) AS VARCHAR)) LIKE :lower_1 || '%') AND (lower(CAST(lower(CAST(gp.customer.name AS VARCHAR)) AS VARCHAR)) LIKE '%' || :lower_2)


Thanks & Regards,

Khalid Khan

Software Engineer

 

 1st Floor, Prabhavee Tech Park, S. No. 125, Baner, Pune 411 045

(+91) 9594497691 | mkkhan@integrichain.com | www.integrichain.com | LinkedIn | IntegriChain Blog

- 1st  issue 68def593ec64
- 2nd issue 3cc34c514f1b -> c76b765f4bbc

d168eb212189


def create_seed_data():
    conn = op.get_bind()
    with open("database/install/insert_sv_seed_data.sql", 'r') as sql: conn.execute(
        text(sql.read()))
        
ADD_HEADER_IN_REPORT

{
    "unbucketed": [],
    "products": {
        "106310100": [
            "10631010030"
        ],
        "106310101": [
            "10631010160"
        ],
        "694890711": [
            "69489071160"
        ],
        "694890721": [
            "69489072105",
            "69489072130"
        ],
        "704280011": [
            "70428001111",
            "70428001112"
        ],
        "721430311": [
            "72143031160"
        ],
        "721430321": [
            "72143032130"
        ]
    },
    "periods": [
        "201909",
        "201906",
        "201903",
        "201812",
        "201809",
        "201806",
        "201803",
        "201712",
        "201709",
        "201706",
        "201703",
        "201612"
    ]
}


2021-04-01 2021-05-31
end_date = datetime.datetime.strptime(str(end), "%Y-%m-%d").strftime("%d-%m-%Y")

GP-986

# GP-988

data... {'startRow': 0, 'endRow': 100, 'filterModel': {}, 'sortModel': [], 'effective_date': ''}
model... <class 'app.gp.models.chargeback.Chargeback'>
columns... [<ColumnDictionary 24011>, <ColumnDictionary 24014>]
lcolumns... {'BilltoNum': <ColumnDictionary 24011>, 'CBKAmount': <ColumnDictionary 24014>}

#
data... {'startRow': 0, 'endRow': 100, 'filterModel': {'Description': {'type': 'contains', 'filter': 'de', 'filterType': 'text'}}, 'sortModel': [], 
'effective_date': ''}

#
filters... {'customer.name': {'type': 'notEqual', 'filter': 'inc', 'filterType': 'text', 'relation_col': 'name'}}
column_op... {'type': 'notEqual', 'filter': 'inc', 'filterType': 'text', 'relation_col': 'name'}

filters... {'customer.name': {'condition1': {'type': 'contains', 'filter': 'eah', 'filterType': 'text'}, 
                              'condition2': {'type': 'startsWith', 'filter': 'lea', 'filterType': 'text'}, 
                              'operator': 'AND', 'relation_col': 'name'}}

column_op... {'condition1': {'type': 'contains', 'filter': 'eah', 'filterType': 'text'}, 
              'condition2': {'type': 'startsWith', 'filter': 'lea', 'filterType': 'text'}, 
              'operator': 'AND', 'relation_col': 'name'}
              
#contains
EXISTS (SELECT 1 
FROM gp.customer, gp.customer_id 
WHERE gp.customer.id = gp.customer_id.customer_id_sparc AND lower(gp.customer.name) LIKE lower(:name_1))

filter_clause... EXISTS (SELECT 1 
FROM gp.customer, gp.customer_id 
WHERE gp.customer.id = gp.customer_id.customer_id_sparc AND lower(gp.customer.name) = :lower_1)


#GP-986
Previous Months Buckets


previous_months_buckets = wb["Previous Months Buckets"]
for y, col in enumerate(bucket_cols, start=1):
previous_months_buckets.cell(row=1, column=y).value = col

namespace = {
    "Decimal": Decimal,
    "month2date": month2date,
    "month2quarter": month2quarter,
    "write_method_str": write_method_str,
    "price_type": price_type,
    "client": client,
}
x = 0  # In case output is empty, set equal to zero
for x, line in enumerate(out, start=2):
    namespace["line"] = line
    for y, col in enumerate(bucket_cols, start=1):
        exec(bucket_cols[col], namespace)
        buckets.cell(row=x, column=y).value = namespace["ret"]

# Appending determined calculation ratio for each period if output exists
if x:
    write_calc_methods(
        buckets, bucket_cols, x + 1, namespace, run_price_type, price_type
    )
    
- model n solution competitor
- price_type_ids = db.session.query(GPPriceType.id).filter_by(
        sb_id=price_type.sb_id
    ).all()

    previous_delivered_bucket = RunPriceType.query.filter(
        and_(
            RunPriceType.price_type_id.in_(price_type_ids),
            RunPriceType.end_period == date_obj,
            RunPriceType.stage == RunPriceTypeStageEnum.DELIVERED,
        )
    ).order_by(RunPriceType.id.desc()).first()
    

https://stackoverflow.com/questions/52238781/postgres-integer-out-of-range-why-this-error-occur

ndc
bucket name
period

price_type_1 [('Data Summary', 2, 'chargebacks'), ('Data Summary', 2, 'sales'), ('Data Summary', 2, 'adjustments'), 
('Data Summary', 2, 'returns'), ('Data Summary', 2, 'free_goods'), ('Data Summary', 2, 'chargeback_payments'), 
('Data Summary', 2, 'cb_chargebacks'), ('Data Summary', 2, 'rebates')]


 # price_type_1 = (RunPriceType.query.join(
        #     GPPriceType, 
        #     GPPriceType.id == RunPriceType.price_type_id,
        #     ).join(
        #         LogicBucket,
        #         LogicBucket.price_type_id == RunPriceType.price_type_id,
        #         ).filter(and_(RunPriceType.id == run_price_type_id_1, 
        #         LogicBucket.derived == False,
        #         LogicBucket.unbucketed == False))
        #         # .with_entities(
        #         #     GPPriceType.name.label("price_type"), 
        #         #     GPPriceType.version, 
        #         #     LogicBucket.name.label("bucket")
        #         #     )
        # )
        # qry = (db.session.query(price_type_1))
        # print("qry", qry)
        # for data in price_type_1:
        #     print("data", data.buckets.name)
        # print("price_type....", price_type.id, price_type.status, price_type.version)
        
 buckets2 = LogicBucket.query.filter(LogicBucket.price_type==price_type_2, and_(LogicBucket.derived==False, 
        LogicBucket.unbucketed==False)).with_entities( 
                    LogicBucket.name,
                    LogicBucket.enabled,
                    LogicBucket.group_key,
                    LogicBucket.variance_threshold_unit,
                    LogicBucket.reportable,
                    LogicBucket.summary,
                    LogicBucket.calc_group,
                    LogicBucket.summary_variance,
                    LogicBucket.variance_threshold_dollar,
                    LogicBucket.dollar_type,
                    LogicBucket.source,
                    LogicBucket.value,
                    LogicBucket.value_period,
                    LogicBucket.reportable_name,
                    LogicBucket.use_cppd,
                    LogicBucket.allow_overlap,
                    ).all()  
                    
formulas1 = Formula.query.filter(Formula.price_type==price_type_1, and_(Formula.derived==False)).with_entities( 
                    Formula.name,
                    Formula.enabled,
                    Formula.variance_threshold_unit,
                    Formula.reportable,
                    Formula.summary,
                    Formula.calc_group,
                    Formula.summary_variance,
                    Formula.variance_threshold_dollar,
                    Formula.d_round,
                    Formula.u_round,
                    Formula.ratio_formula,
                    Formula.minimum,
                    Formula.deliverable,
                    Formula.reportable_name,
                    Formula.no_rollup,
                    Formula.value_period,
                    Formula.units_value,
                    Formula.period,
                    Formula.level,
                    Formula.dollars_value
                    ).all()  
            
        
        
{'date_ds': 'period_date', 'report_template': {'modified_user': {'name': 'Janice Lee', 'id': 14}, 
'filepath': '/usr/src/app/upload/a61083b2-170e-4cf7-91ff-bb96301e2854.xlsm', 'id': 22, 'scan_error': False, 
'scanned': True, 'modified_on': '2021-10-28 13:35:27.999936', 'modified_on_tmz': '2021-10-28 09:35', 'price_type_id': 22, 
'filename': 'Adamas data_summary Report Template (1).xlsm'}, 'approved_by': 63, 'price_type': 'DATA_SUMMARY', 
'modifying_user': {'name': "Nick O'Brien", 'id': 63}, 'version': 2, 'date_tri': 'period_date', 'client_id': 7, 
'modified_on': '2020-03-13 17:57:54.036870 UTC', 'modified_on_tmz': '2020-03-13 13:57', 'name': 'Data Summary', 
'redo_count': 0, 'date_reb': 'period_date', 'date_cbk': 'period_date', 'approval': None, 'id': 22, 'sb_id': 13, 
'undo_count': 1, 'errors': [], 'modified_by': 63, 'approved_on': '2020-03-13 17:57:54.036830', 
'approving_user': {'name': "Nick O'Brien", 'id': 63}, 'ppd_column': 'tppd', 'ordering': 0, 'status': 'ACTIVE', 
'buckets_and_formulas': [{'allow_overlap': False, 'value_period': 'DEFAULT', 'enabled': True, 'price_type_id': 22, 
'reportable_name': 'CB Chargebacks', 'unbucketed': False, 'use_cppd': False, 'group_key': None, 'logic_master_id': None, 
'name': 'cb_chargebacks', 'variance_threshold_dollar': '0.0000', 'derived': False, 'labeler_variances': [], 'value': "TransType.Class = 'cb'", 
'summary_variance': False, 'id': 613, 'reportable': False, 'errors': [], 'summary': False, 'dollar_type': 'NET_AMOUNT', 
'source': 'DS', 'ordering': 1, 'variance_threshold_unit': '0.0000', 'calc_group': 'STANDARD', '_type': 'BUCKET', 'type': 'Bucket (DS)'}, 
{'allow_overlap': False, 'value_period': 'DEFAULT', 'enabled': True, 'price_type_id': 22, 'reportable_name': 'Chargeback Payments', 
'unbucketed': False, 'use_cppd': False, 'group_key': None, 'logic_master_id': None, 'name': 'chargeback_payments', 
'variance_threshold_dollar': '0.0000', 'derived': False, 'labeler_variances': [], 'value': "TransType.Class = 'chargeback'", 'summary_variance': False, 'id': 612, 'reportable': False, 'errors': [], 'summary': False, 'dollar_type': 'NET_AMOUNT', 'source': 'DS', 'ordering': 2, 'variance_threshold_unit': '0.0000', 'calc_group': 'STANDARD', '_type': 'BUCKET', 'type': 'Bucket (DS)'}, {'allow_overlap': False, 'value_period': 'DEFAULT', 'enabled': True, 'price_type_id': 22, 'reportable_name': 'Free Goods', 'unbucketed': False, 'use_cppd': False, 'group_key': None, 'logic_master_id': None, 'name': 'free_goods', 'variance_threshold_dollar': '0.0000', 'derived': False, 'labeler_variances': [], 'value': "TransType.Class = 'free_good'", 'summary_variance': False, 'id': 611, 'reportable': False, 'errors': [], 'summary': False, 'dollar_type': 'NET_AMOUNT', 'source': 'DS', 'ordering': 3, 'variance_threshold_unit': '0.0000', 'calc_group': 'STANDARD', '_type': 'BUCKET', 'type': 'Bucket (DS)'}, {'allow_overlap': False, 'value_period': 'DEFAULT', 'enabled': True, 'price_type_id': 22, 'reportable_name': 'Returns', 'unbucketed': False, 'use_cppd': False, 'group_key': None, 'logic_master_id': None, 'name': 'returns', 'variance_threshold_dollar': '0.0000', 'derived': False, 'labeler_variances': [], 'value': "TransType.Class = 'return'", 'summary_variance': False, 'id': 610, 'reportable': False, 'errors': [], 'summary': False, 'dollar_type': 'NET_AMOUNT', 'source': 'DS', 'ordering': 4, 'variance_threshold_unit': '0.0000', 'calc_group': 'STANDARD', '_type': 'BUCKET', 'type': 'Bucket (DS)'}, {'allow_overlap': False, 'value_period': 'DEFAULT', 'enabled': True, 'price_type_id': 22, 'reportable_name': 'Adjustments', 'unbucketed': False, 'use_cppd': False, 'group_key': None, 'logic_master_id': None, 'name': 'adjustments', 'variance_threshold_dollar': '0.0000', 'derived': False, 'labeler_variances': [], 'value': "TransType.Class = 'adjust'", 'summary_variance': False, 'id': 609, 'reportable': False, 'errors': [], 'summary': False, 'dollar_type': 'NET_AMOUNT', 'source': 'DS', 'ordering': 5, 'variance_threshold_unit': '0.0000', 'calc_group': 'STANDARD', '_type': 'BUCKET', 'type': 'Bucket (DS)'}, {'allow_overlap': False, 'value_period': 'DEFAULT', 'enabled': True, 'price_type_id': 22, 'reportable_name': 'Sales', 'unbucketed': False, 'use_cppd': False, 'group_key': None, 'logic_master_id': None, 'name': 'sales', 'variance_threshold_dollar': '0.0000', 'derived': False, 'labeler_variances': [], 'value': "TransType.Class = 'sale'", 'summary_variance': False, 'id': 608, 'reportable': True, 'errors': [], 'summary': True, 'dollar_type': 'NET_AMOUNT', 'source': 'DS', 'ordering': 6, 'variance_threshold_unit': '0.0000', 'calc_group': 'STANDARD', '_type': 'BUCKET', 'type': 'Bucket (DS)'}, {'allow_overlap': False, 'value_period': 'DEFAULT', 'enabled': True, 'price_type_id': 22, 'reportable_name': 'Chargebacks', 'unbucketed': False, 'use_cppd': False, 'group_key': None, 'logic_master_id': None, 'name': 'chargebacks', 'variance_threshold_dollar': '0.0000', 'derived': False, 'labeler_variances': [], 'value': 'Chargeback.Quantity >= 0 OR Chargeback.Quantity <= 0', 'summary_variance': False, 'id': 607, 'reportable': True, 'errors': [], 'summary': False, 'dollar_type': 'CBK_AMOUNT', 'source': 'CBK', 'ordering': 7, 'variance_threshold_unit': '0.0000', 'calc_group': 'STANDARD', '_type': 'BUCKET', 'type': 'Bucket (CBK)'}, {'allow_overlap': False, 'value_period': 'DEFAULT', 'enabled': True, 'price_type_id': 22, 'reportable_name': 'Rebates', 'unbucketed': False, 'use_cppd': False, 'group_key': None, 'logic_master_id': None, 'name': 'rebates', 'variance_threshold_dollar': '0.0000', 'derived': False, 'labeler_variances': [], 'value': '1 = 1', 'summary_variance': False, 'id': 606, 'reportable': True, 'errors': [], 'summary': False, 'dollar_type': 'NET_AMOUNT', 'source': 'REB', 'ordering': 8, 'variance_threshold_unit': '0.0000', 'calc_group': 'STANDARD', '_type': 'BUCKET', 'type': 'Bucket (REB)'}]}