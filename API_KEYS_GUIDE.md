# 🔑 FREE API KEYS SETUP GUIDE
## Get all API keys in 15 minutes!

---

## 🎯 Required APIs (Essential)

### 1. Groq (Primary LLM - Ultra Fast!) ⭐⭐⭐⭐⭐
**What**: Ultra-fast AI inference (Llama 3.3 70B)
**Free Tier**: ~14,000 requests/day (very generous!)
**Signup**: [https://console.groq.com/](https://console.groq.com/)

#### Steps:
1. Visit https://console.groq.com/
2. Click "Sign Up" (use Google/GitHub for quick signup)
3. Go to "API Keys" in the dashboard
4. Click "Create API Key"
5. Copy the key (starts with `gsk_...`)
6. Add to `.env`: `GROQ_API_KEY=gsk_...`

**Time**: 2 minutes ⏱️

---

### 2. Serper (Google Search) ⭐⭐⭐⭐⭐
**What**: Google Search API
**Free Tier**: 2,500 searches/month
**Signup**: [https://serper.dev/](https://serper.dev/)

#### Steps:
1. Visit https://serper.dev/
2. Click "Sign Up"  (use Google for quick signup)
3. Dashboard will show your API key immediately
4. Copy the key
5. Add to `.env`: `SERPER_API_KEY=your_key_here`

**Time**: 2 minutes ⏱️

---

### 3. Tavily (AI Research) ⭐⭐⭐⭐
**What**: AI-powered research API
**Free Tier**: 1,000 searches/month
**Signup**: [https://tavily.com/](https://tavily.com/)

#### Steps:
1. Visit https://tavily.com/
2. Click "Get API Key" / "Sign Up"
3. Create account
4. Go to dashboard → API Keys
5. Copy your API key
6. Add to `.env`: `TAVILY_API_KEY=tvly-...`

**Time**: 2 minutes ⏱️

---

## 📍 Optional APIs (Recommended)

### 4. Brave Search ⭐⭐⭐
**What**: Alternative search engine
**Free Tier**: 2,000 searches/month
**Signup**: [https://brave.com/search/api/](https://brave.com/search/api/)

#### Steps:
1. Visit https://brave.com/search/api/
2. Click "Get Started"
3. Fill application form
4. Wait for approval email (usually instant)
5. Get API key from dashboard
6. Add to `.env`: `BRAVE_SEARCH_API_KEY=BSA...`

**Time**: 5 minutes ⏱️

---

### 5. ScraperAPI (Web Scraping) ⭐⭐⭐
**What**: Web scraping with proxies
**Free Tier**: 1,000 requests/month
**Signup**: [https://www.scraperapi.com/](https://www.scraperapi.com/)

#### Steps:
1. Visit https://www.scraperapi.com/
2. Click "Get Started Free"
3. Sign up
4. Dashboard shows API key
5. Copy the key
6. Add to `.env`: `SCRAPER_API_KEY=your_key_here`

**Time**: 2 minutes ⏱️

---

### 6. NewsAPI (Latest News) ⭐⭐
**What**: News articles from 80,000+ sources
**Free Tier**: 1,000 requests/day (developer plan)
**Signup**: [https://newsapi.org/](https://newsapi.org/)

#### Steps:
1. Visit https://newsapi.org/
2. Click "Get API Key"
3. Register (choose free "Developer" plan)
4. Verify email
5. Get API key from account page
6. Add to `.env`: `NEWS_API_KEY=your_key_here`

**Time**: 3 minutes ⏱️

---

## 💰 Totally Optional (For Advanced Features)

### 7. DeepSeek (Backup LLM)
**What**: Alternative AI model
**Free Tier**: $5 free credits
**Signup**: [https://platform.deepseek.com/](https://platform.deepseek.com/)

### 8. Stability AI (Image Generation)
**What**: Generate AI images for infographics
**Free Tier**: Limited credits
**Signup**: [https://stability.ai/](https://stability.ai/)

### 9. Unsplash (Stock Photos)
**What**: High-quality stock images
**Free Tier**: 50 requests/hour
**Signup**: [https://unsplash.com/developers](https://unsplash.com/developers)

---

## ✅ Quick Setup Checklist

### Minimum Required (3 APIs - 6 minutes):
- [ ] Groq API (2 min)
- [ ] Serper API (2 min)
- [ ] Tavily API (2 min)

### Recommended (6 APIs - 15 minutes):
- [ ] Groq API ⭐⭐⭐⭐⭐
- [ ] Serper API ⭐⭐⭐⭐⭐
- [ ] Tavily API ⭐⭐⭐⭐
- [ ] Brave Search API ⭐⭐⭐
- [ ] ScraperAPI ⭐⭐⭐
- [ ] NewsAPI ⭐⭐

---

## 📝 After Getting Keys

### 1. Create `.env` file:
```bash
cd research-agent-pro/backend
cp .env.example .env
```

### 2. Add your keys to `.env`:
```bash
# Required
GROQ_API_KEY=gsk_your_groq_key_here
SERPER_API_KEY=your_serper_key_here
TAVILY_API_KEY=tvly-your_tavily_key_here

# Optional but recommended
BRAVE_SEARCH_API_KEY=BSA_your_brave_key_here
SCRAPER_API_KEY=your_scraper_key_here
NEWS_API_KEY=your_news_key_here
```

### 3. Test the setup:
```bash
# Start backend
cd backend
python app/main.py

# Visit http://localhost:8000/health
# Should show all API keys as ✅
```

---

## 💡 Pro Tips

### 1. Use Multiple Search APIs
Combine Serper + Tavily + Brave for best results:
- **Serper**: Fast, Google-quality results
- **Tavily**: Deep research, AI-optimized
- **Brave**: Privacy-focused, different results

### 2. Monitor Usage
All services have dashboards to track:
- Requests used
- Remaining quota
- Cost (if you upgrade)

### 3. Rate Limiting
The app automatically handles rate limits and switches between APIs!

### 4. Backup APIs
Always configure at least 2 search APIs for redundancy.

---

## 🚨 Troubleshooting

### "API key not configured"
- Check `.env` file exists in `backend/` folder
- Ensure no spaces around `=` in `.env`
- Restart the backend server

### "Invalid API key"
- Double-check you copied the entire key
- Some keys have prefixes (`gsk_`, `tvly-`, `BSA_`)
- Regenerate key if needed

### "Rate limit exceeded"
- Wait for quota reset (usually daily/monthly)
- Add additional API as backup
- Upgrade to paid tier if needed

---

## 📊 Free Tier Capacity

With all free tiers combined, you can do:

**Per Month**:
- ~6,000 searches (Serper 2.5k + Brave 2k + Tavily 1k + others)
- ~420,000 LLM requests (Groq ~14k/day × 30 days)
- ~30,000 news requests (NewsAPI 1k/day × 30 days)
- ~1,000 scraping requests (ScraperAPI)

**Practical Capacity**:
- 📊 **~500 research queries/day** (completely FREE!)
- 📈 **~15,000 research queries/month**

That's better than $20/month Perplexity Pro! 🎉

---

## 🎯 Next Steps

Once you have your API keys:

1. ✅ Add them to `.env`
2. ✅ Start the backend: `python app/main.py`
3. ✅ Check health: http://localhost:8000/health
4. ✅ Start frontend: `npm run dev`
5. ✅ Start researching!

---

**Got all your keys? Great! Let's build something amazing! 🚀**
