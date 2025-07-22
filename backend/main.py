from fastapi import FastAPI,status,HTTPException
from youtube_transcript_api import YouTubeTranscriptApi
from youtubesearchpython import VideosSearch


app = FastAPI()


@app.get("/",status_code=status.HTTP_200_OK)
def health_check():
    return {"Backend Running Smooth as hell.."}

@app.post("/yt_transcript",status_code=status.HTTP_201_CREATED)
def get_yt_transcript(keyword:str):
    urls = get_video_links(keyword)
    videoIds = get_videoId(urls)
    transcripts = get_video_transcript(videoIds)

    return {'transcripts':transcripts}



def get_video_links(keyword_search:str,top_k:int = 3):
    videosSearch = VideosSearch(keyword_search, limit = top_k)
    response = videosSearch.result()
    yt_links = []

    for res in response['result']:
        yt_links.append(res['link'])

    return yt_links


def get_videoId(urls:str):
    ids = []
    for url in urls:
        ids.append(url.split("?v=")[-1])

    return ids

def get_video_transcript(video_ids:str):
    transcripts = []

    for v_id in video_ids:
        ytt_api = YouTubeTranscriptApi()
        response = ytt_api.fetch(v_id)

        transcript = ""
        for res in response.snippets:
            transcript += res.text
        
        transcripts.append(transcript)

    return transcripts