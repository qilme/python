(*a,)=eval(input('请输入逗号分隔的多个数据：'))
mm=lambda x:(max(x),min(x))#①
print('最大最小值元组：', mm(a))#②
