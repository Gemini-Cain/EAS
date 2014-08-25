#@Date 2014/08/25
#@Author Xin Du
#coding: utf-8


product_capability_dict = {'0001':'账户能力', '0002':'银行网关能力', '0003':'业务网关能力'}
product_line_dict = {'01':'资金归集', '02':'交费易'}
product_type_dict = {'01':'充值', '02':'提现', '03':'转账', '04':'消费'}

def GenerateAction():
	product_capability = ''
	action_name = ''
	while product_capability == '' or product_line not in product_capability_dict.keys():
		product_capability = raw_input('请输入业务能力提供方<账户能力0001，银行网关能力0002，业务网关能力0003>:'.decode('utf-8').encode('gbk'))
	while action_name == '' :
		action_name = raw_input('请输入业务名称：'.decode('utf-8').encode('gbk'))
	action_code = product_capability + '0000'
	print action_name.decode('utf-8') + ':' + action_code

def GenerateProduct():
	product_line = ''
	product_name = ''
	product_type = ''
	while product_line == '' or product_line not in product_line_dict.keys():
		product_line = raw_input('请输入产品线<资金归集01,交费易02>:'.decode('utf-8').encode('gbk'))
	while product_name == '' :
		product_name = raw_input('请输入产品名称：'.decode('utf-8').encode('gbk'))
	while product_type == '' or product_type not in product_type_dict.keys():
		product_type = raw_input('请输入业务类型（充值01，提现02，转账03，消费04）:'.decode('utf-8').encode('gbk'))
	product_code = product_line + product_type + '0000'
	print product_name.decode('utf-8') + ':' + product_code

def test():
	GenerateAction()

if __name__ == '__main__':
	test()

Insert into EXPORT_TABLE (ACTION_ID,ACTION_CODE,ACTION_NAME,CAT_ID,PROD_ID,PRTN_ID,ACTION_TYPE,FRONT_BACK_FLAG,EFF_DATE,EXP_DATE,ISSUE_NAME,ISSUE_DATE,MEMO,STAT,STAT_REASON,ACTION_FRONT_BACK_FLAG,PDLINE_TYPE) values (1,'01010001','授权银行卡充值',103,100,null,'CHARGE','B',null,null,null,null,'正式数据','S0A','0000000000','BIG',null);