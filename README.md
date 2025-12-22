# VSMS - Versatile Safety Management System

A comprehensive, AI-powered safety management system designed for workplaces to streamline EHS (Environment, Health, and Safety) processes, reduce incidents, and create safer work environments.

## 🌟 Key Features

### 🤖 AI-Powered Safety Analysis
- **Intelligent Safety Guard**: AI-driven hazard identification and risk assessment
- **Multi-Modal Input**: Analyze safety risks using:
  - Text descriptions
  - Image uploads (photos of work areas)
  - Voice recordings (voice-to-text transcription)
- **Instant HIRA Generation**: Get professional Hazard Identification and Risk Assessment reports in seconds
- **Real-time Analysis**: Powered by advanced AI models for accurate risk detection

### 👥 User Management
- **Role-Based Access Control**: Admin, Safety Manager, Supervisor, and Employee roles
- **User Dashboard**: Real-time user statistics and management
- **Group Management**: Create and manage teams with customizable permissions
- **Approval Workflow**: Employee approval system for access control

### ⚠️ Hazard Management (HIRA)
- **Real-time Hazard Reporting**: Quick and easy hazard identification
- **AI Analysis Integration**: Click "AI Analysis" button to use AI-powered assessment
- **Multi-Level Approval**: Admin, Manager, and Supervisor approval workflow
- **Priority Assignment**: Assign priority levels and timelines
- **Team Assignment**: Assign hazards to specific teams
- **Status Tracking**: Track hazards from Open → Pending → Approved → Resolved

### ✅ Safety Checklists
- **Customizable Templates**: Create checklists for different departments
- **Digital Completion**: Complete checklists digitally with timestamps
- **Progress Tracking**: Monitor checklist completion rates
- **Role-Based Access**: Different checklists for different roles

### 📊 Analytics & Reporting
- **Interactive Dashboards**: Role-specific dashboards with key metrics
- **Visual Charts**: Recharts-powered data visualization
- **Trend Analysis**: Track safety performance over time
- **Export Reports**: Download reports in PDF, Word, JPG, and JSON formats

### 🔔 Notifications & Alerts
- **Real-time Alerts**: Instant notifications for safety concerns
- **Group Notifications**: Team-specific alerts
- **Hazard Updates**: Automatic notifications for hazard status changes
- **Training Reminders**: Automated training schedule notifications

### 🎓 Training Management
- **Course Tracking**: Manage employee training programs
- **Completion Monitoring**: Track training completion status
- **Certification Management**: Store and manage safety certifications
- **Scheduled Training**: Plan and schedule training sessions

### 🏆 Rewards System
- **Safety Recognition**: Reward employees for safety compliance
- **Point System**: Track safety points and achievements
- **Leaderboards**: Encourage safety culture through gamification

### 🎨 Modern UI/UX
- **Dark/Light Mode**: Customizable theme preferences
- **Responsive Design**: Optimized for desktop, tablet, and mobile
- **Intuitive Navigation**: Easy-to-use interface
- **Accessible**: WCAG compliant design

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 18 with Vite
- **Styling**: Tailwind CSS with shadcn/ui components
- **Routing**: React Router DOM (HashRouter for compatibility)
- **State Management**: React Context API
- **Data Fetching**: TanStack Query (React Query)
- **Charts**: Recharts
- **Theme**: next-themes
- **Icons**: Lucide React
- **Forms**: React Hook Form with Zod validation
- **Language**: JavaScript (ES6+)

### Backend
- **Framework**: FastAPI (Python)
- **AI/ML**: Google Gemini AI for safety analysis
- **Image Processing**: PIL (Python Imaging Library)
- **Audio Processing**: Speech recognition for voice-to-text
- **API**: RESTful API with automatic OpenAPI documentation
- **CORS**: Enabled for frontend-backend communication

## 📋 Prerequisites

- **Node.js**: Version 16 or higher
- **Python**: Version 3.8 or higher
- **npm** or **yarn**: Package manager
- **pip**: Python package manager

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone <YOUR_GIT_URL>
cd safty
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Set up environment variables (create .env file)
# Add your Google Gemini API key:
# GOOGLE_API_KEY=your_api_key_here

# Start the backend server
python -m uvicorn main:app --reload --port 8000
```

The backend will be available at `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd safetyfrontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 👤 Demo Accounts

Use these credentials to test different user roles:

| Role | Email | Password |
|------|-------|----------|
| **Admin** | admin@company.com | 1122 |
| **Safety Manager** | manager@company.com | 1122 |
| **Supervisor** | supervisor@company.com | 1122 |
| **Employee** | employee@company.com | 1122 |

## 📁 Project Structure

```
safty/
├── backend/                    # FastAPI backend
│   ├── main.py                # Main application entry
│   ├── requirements.txt       # Python dependencies
│   └── ...                    # Other backend files
│
├── safetyfrontend/            # React frontend
│   ├── src/
│   │   ├── components/        # Reusable UI components
│   │   │   ├── layout/       # Layout components
│   │   │   └── ui/           # shadcn/ui components
│   │   ├── contexts/         # React contexts
│   │   ├── pages/            # Page components
│   │   │   ├── Index.jsx     # AI Assessment page
│   │   │   ├── InputPanel.jsx # AI input interface
│   │   │   ├── ResultsPanel.jsx # AI results display
│   │   │   ├── Hazards.jsx   # Hazard management
│   │   │   └── ...           # Other pages
│   │   ├── lib/              # Utility functions
│   │   ├── App.jsx           # Main App component
│   │   └── main.jsx          # Entry point
│   ├── package.json          # Dependencies
│   └── vite.config.js        # Vite configuration
│
└── README.md                  # This file
```

## 🎯 User Roles & Permissions

### Admin
- Full system access
- User management and approval
- System settings configuration
- View all dashboards and reports
- Manage groups and departments

### Safety Manager
- Hazard management and approval
- Incident tracking and analysis
- Analytics and reporting
- Training management
- Team oversight

### Supervisor
- Team management
- Checklist oversight
- Hazard review and approval
- Training coordination
- Group management

### Employee
- Hazard reporting
- AI safety analysis
- Checklist completion
- Training participation
- View personal dashboard (after approval)

## 🔧 Available Scripts

### Frontend
```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run preview      # Preview production build
npm run lint         # Run ESLint
```

### Backend
```bash
python -m uvicorn main:app --reload --port 8000  # Start dev server
python -m uvicorn main:app --port 8000           # Start production server
```

## 🌐 API Endpoints

### AI Analysis
- `POST /assess` - Perform AI safety assessment
- `POST /transcribe` - Transcribe voice to text
- `POST /report` - Generate safety report
- `GET /report/pdf` - Download PDF report

### Documentation
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

## 🎨 Features in Detail

### AI Hazard Analysis
1. Navigate to Hazard Management page
2. Click "AI Analysis" button
3. Choose input method:
   - Type activity description
   - Upload photo of work area
   - Record voice note
4. Click "Perform Risk Assessment"
5. View AI-generated results with:
   - Identified hazards
   - Risk levels
   - Safety recommendations
   - Control measures
6. Download report in multiple formats

### Hazard Workflow
1. **Employee Reports** → Hazard created with "Open" status
2. **Admin Reviews** → Sends to approval (status: "Pending")
3. **Manager Approves** → Adds priority and timeline
4. **Supervisor Approves** → Assigns team
5. **All Approved** → Status changes to "Approved"
6. **Team Resolves** → Status changes to "Resolved"

## 🚢 Deployment

### Frontend (Vercel/Netlify)
1. Build the project: `npm run build`
2. Deploy the `dist` folder
3. Set base path in `vite.config.js` if needed

### Backend (Heroku/Railway/Render)
1. Add `Procfile` with: `web: uvicorn main:app --host 0.0.0.0 --port $PORT`
2. Set environment variables (GOOGLE_API_KEY)
3. Deploy from Git repository

## 🔒 Security Features

- Role-based access control (RBAC)
- Protected routes with authentication
- Input validation and sanitization
- Secure API endpoints
- Environment variable protection

## 🐛 Troubleshooting

### Frontend not loading?
- Hard refresh: `Ctrl + Shift + R`
- Clear browser cache
- Check console for errors
- Ensure backend is running

### Backend connection issues?
- Verify backend is running on port 8000
- Check CORS settings
- Verify API endpoint URLs in frontend

### AI Analysis not working?
- Ensure GOOGLE_API_KEY is set in backend
- Check backend logs for errors
- Verify internet connection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 📧 Support

For support, email support@vsms.com or create an issue in the repository.

## 🙏 Acknowledgments

- shadcn/ui for the beautiful component library
- Lucide React for the icon set
- Google Gemini AI for powering the safety analysis
- FastAPI for the robust backend framework
- React and Vite for the modern frontend stack

---

**Built with ❤️ for safer workplaces**
#   s a f t y  
 #   s a f t y  
 