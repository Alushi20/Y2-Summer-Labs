def create_youtube_video(title,description,list):
		video={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{"username":""},"hashtag":}
		return video
def like (youtube_video):
	if("likes" in youtube_video):
		youtube_video["likes"]=+1
	return youtube_video

def dislikes (youtube_video):
	if("dislikes" in youtube_video):
		youtube_video["dislikes"]+=1
	return youtube_video

def add_comment(youtubevideo,username,comment_text):
	youtube_video["comments"]={username:comment_text}
	return youtubevideo

vidvid=create_youtube_video("mee at the zoo","zooooo")
vidvid=like(vidvid)
vidvid=dislikes(vidvid)
for i in range (495):
	like(vidvid)


def similarity_to_video (vid1,vid2):
	c=0
	for i in vid2["hashtag"]:
		for j in vid1["hashtag"]:
			if(i==j):
				c+=1
	return(c*0.2)


