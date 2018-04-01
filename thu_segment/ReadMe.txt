语料 信息
1. 用户关系 - weibo_follows.csv 
	结构: followerid , userid 
	解释: 粉丝ID , 用户ID
2. 用户信息 - weibo_users.csv
	结构: verified,name,gender,location,user_id,description
	解释: 是否认证 ,用户名,用户性别,地点,用户ID,用户描述 
3. 微博信息 目录 /merge下 csv 文件
	结构: userid,reposts_count,comment_count,source,created_at, text
	解释: 用户ID,转发数,评论数,来源,创建时间,文本内容
	示例:
		1427624332,0,0,新浪博客,2012-10-14 00:08,分享自康斯坦丁  《麻省理工揭秘：时间旅行真正的秘密》 -
