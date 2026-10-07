from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from google import genai
import os
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
app = FastAPI()
@app.get("/", response_class=HTMLResponse)
def home():
    return """<html dir='rtl' style='background:#111;color:#fff;text-align:center;padding:30px;font-family:tahoma'><h1>✅ موقعي شغال!</h1><input id=q style='width:70%;padding:15px;border-radius:10px' placeholder='اسأل أي حاجة...'><button onclick="ask()" style='padding:15px;background:#0f0;border-radius:10px'>اسأل</button><p id=a style='margin-top:20px;white-space:pre-wrap;background:#222;padding:15px;border-radius:10px'></p><script>async function ask(){document.getElementById('a').innerText='⏳ بفكر...';let r=await fetch('/ai?q='+encodeURIComponent(document.getElementById('q').value));let d=await r.json();document.getElementById('a').innerText=d.answer;}</script></html>"""
@app.get("/ai")
def ai(q: str):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=q)
    return {"answer": response.text}
