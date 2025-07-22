#%%
from langchain_community.document_loaders import YoutubeLoader

#%%
url = "https://www.youtube.com/watch?v=73h5Lb_N9r8"


loader = YoutubeLoader.from_youtube_url(
    url, add_video_info=False
)

#%%
loader.load()