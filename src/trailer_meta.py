"""Fill in the trailer's English description and Japanese title/description (run with action trailer_meta)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import upload as up

ROOT = up.ROOT
vid = json.load(open(os.path.join(ROOT, "trailer.json")))["video_id"]
pid = json.load(open(os.path.join(ROOT, "playlist.json")))["id"]
EP1 = "hj8EgYR2ORo"
TITLE_EN = "Can AI Replace Me? Start Here | Human Curriculum English Podcast"
TITLE_JA = "AIに仕事を奪われる？東京のセナがシアトルのメンターに出会うまで｜Human Curriculum"
DESC_EN = f"""If AI can do your job, what's left for you?

Sena, an Associate in Tokyo, dreams of leading people in the US. So she finds a mentor in Seattle: Daniel, a People Manager. This is how Human Curriculum began.

▶ Start with Episode 1: https://youtu.be/{EP1}
📚 All episodes, in order: https://www.youtube.com/playlist?list={pid}

Human Curriculum | Learn what AI can't do, in natural English.
Real situations, real research, and one challenge you can try at work today. Captions in English and Japanese.

Sena and Daniel are fictional characters. Their voices are AI-generated.

#EnglishPodcast #EQ #CareerGrowth #AI"""
DESC_JA = f"""AIが仕事をこなせるなら、私に何が残る？

東京で働くアソシエイトのセナは、いつかアメリカで人を率いるのが夢。そこで、シアトルのピープルマネージャー・ダニエルにメンターをお願いします。これが Human Curriculum のはじまりです。

▶ まずは第1話から: https://youtu.be/{EP1}
📚 全話を順番に聴く: https://www.youtube.com/playlist?list={pid}

Human Curriculum｜AIにできない人間の力（EQ）を、自然な英語で。
リアルな職場の場面、研究、そして今日すぐ試せるチャレンジを1つ。字幕（CC）は英語・日本語に対応しています。

※セナとダニエルは架空の人物で、声はAIです。

#英語学習 #EQ #キャリア #AI"""

yt = up.youtube()
cur = yt.videos().list(part="snippet,status", id=vid).execute()["items"][0]
sn = cur["snippet"]
sn.update(title=TITLE_EN, description=DESC_EN, defaultLanguage="en")
body = {"id": vid, "snippet": sn,
        "localizations": {"en": {"title": TITLE_EN, "description": DESC_EN},
                          "ja": {"title": TITLE_JA, "description": DESC_JA}}}
yt.videos().update(part="snippet,localizations", body=body).execute()
print(f"updated https://youtu.be/{vid}")
