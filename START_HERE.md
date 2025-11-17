# 🚀 START HERE - Research Agent Pro

## ⚡ Quick Start (3 Steps)

### Step 1: Get API Keys (5 minutes)

You already have:
- ✅ Groq API
- ✅ DeepSeek API

**Get 2 more** (see `QUICK_API_SETUP.md`):
- Serper API (2 min) - https://serper.dev/
- Tavily API (3 min) - https://tavily.com/

Add them to `backend/.env`

---

### Step 2: Install Dependencies

**Backend:**
```bash
cd backend
pip install -r requirements.txt
```

**Frontend:**
```bash
cd frontend
npm install
```

---

### Step 3: Run the App

**Open 2 terminals:**

**Terminal 1 - Backend:**
```bash
cd backend
python -m uvicorn app.main:app --reload
```
Backend runs on: http://localhost:8000

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```
Frontend runs on: http://localhost:3000

---

## 🎨 See It In Action!

1. Open http://localhost:3000
2. Enter a query like: "AI startup funding trends 2024"
3. Watch beautiful charts generate automatically!

---

## 📊 What You'll See

- **Home Page**: Beautiful search interface
- **Results Page**:
  - Line charts (trends)
  - Bar charts (comparisons)
  - Pie charts (distributions)
  - AI-generated insights
  - Export options (PDF, PowerPoint, PNG)

---

## 🛠️ Troubleshooting

### "Module not found"
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

### "Port already in use"
```bash
# Kill process on port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Kill process on port 3000
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

### "API key not configured"
- Check `backend/.env` file exists
- Make sure you added your API keys
- Restart backend server

---

## 📁 Project Structure

```
research-agent-pro/
├── backend/          # FastAPI + Python
│   ├── app/
│   │   └── main.py  # Run this
│   └── .env         # Your API keys here
│
├── frontend/         # Next.js + React
│   ├── app/
│   └── package.json
│
└── README.md        # Full documentation
```

---

## 🎯 Next Steps

1. ✅ Get API keys
2. ✅ Install dependencies
3. ✅ Run the app
4. ✅ Try example queries
5. ✅ Push to GitHub
6. ✅ Deploy to production
7. ✅ Share with recruiters!

---

**Let's make your GitHub profile shine! 🌟**
