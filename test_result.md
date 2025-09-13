# AgentScope Studio - Development Environment Setup Guide

## Project Overview
**AgentScope Studio** is a powerful local visualization toolkit for agent application development, supporting project management, runtime visualization, tracing, and agent evaluation. It includes a built-in Copilot named "Friday" for development assistance.

### Original User Problem Statement
Create a dev environment, install agentscope-studio and run it for manual testing through the Emergent Preview screen.

## Project Architecture

### Technology Stack
- **Frontend**: React 19 + Vite + Tailwind CSS + Ant Design
- **Backend**: Node.js + Express + TypeORM + SQLite  
- **Python Components**: AgentScope framework integration
- **Package Management**: npm with workspaces (monorepo structure)

### Directory Structure
```
/app/
├── packages/
│   ├── client/          # React frontend (Vite)
│   ├── server/          # Node.js backend (Express + TypeORM)
│   ├── app/             # Python AgentScope components
│   └── shared/          # Common utilities
├── bin/cli.js           # CLI entry point
├── package.json         # Root workspace configuration
└── assets/              # Documentation assets (GIFs)
```

### Service Ports
- **Frontend (Vite)**: http://localhost:5173
- **Backend (Express)**: http://localhost:3000  
- **Database**: SQLite at `/root/AgentScope-Studio/database.sqlite`

## Setup Instructions

### 1. Install Dependencies

**Critical Dependency Issue Resolution:**
The project has a peer dependency conflict:
- Client package requires: `i18next@24.2.3`
- react-i18next@15.7.3 requires: `i18next >= 25.4.1`

**Solution:**
```bash
cd /app
npm install --legacy-peer-deps
npm install reflect-metadata --legacy-peer-deps
```

**Python Dependencies:**
```bash
cd /app/packages/app
pip install -r requirements.txt
```

### 2. Run Development Server

```bash
cd /app
npm run dev
```

This will concurrently start:
- Frontend on port 5173 (Vite)
- Backend on port 3000 (Express)

### 3. Verify Services

**Check Process Status:**
```bash
ps aux | grep -E "(node|vite)" | grep -v grep
```

**Check Logs:**
```bash
tail -f /app/server.log
```

**Expected Log Output:**
```
Frontend:
  VITE v6.3.6  ready in 2675 ms
  ➜  Local:   http://localhost:5173/

Backend:
Database initialized with options: {
  "type": "sqlite",
  "database": "/root/AgentScope-Studio/database.sqlite",
  "synchronize": true,
  "logging": false
}
Server running on port 3000 in development mode ...
```

## Available Features

### Core Functionality
1. **Home & Dashboard** - Main interface navigation
2. **AS-Friday Copilot** - Built-in development assistant & playground  
3. **Project Management** - Agent application project handling
4. **Runtime Visualization** - Real-time agent behavior monitoring
5. **Tracing & Evaluation** - Agent performance analysis
6. **API Documentation** - Integration guides and tutorials
7. **Community Integration** - GitHub, Discord, DingTalk links

### Key UI Elements
- **Left Sidebar Navigation**: Home, Dashboard, Apps, Docs, Community
- **AS-Friday**: Built-in Copilot for development assistance
- **Tutorial & API**: Documentation sections
- **Clean Material Design**: Professional interface with Ant Design components

## Troubleshooting

### Common Issues

**1. reflect-metadata Missing Error:**
```
Error: Cannot find module 'reflect-metadata'
```
**Solution:** `npm install reflect-metadata --legacy-peer-deps`

**2. Dependency Resolution Conflicts:**
```
npm error ERESOLVE unable to resolve dependency tree
```
**Solution:** Use `--legacy-peer-deps` flag for all npm installs

**3. Backend Not Starting:**
- Check if reflect-metadata is installed
- Verify TypeORM dependencies are properly resolved
- Restart with `pkill -f "npm run dev" && npm run dev`

**4. Database Issues:**
- SQLite database auto-initializes on first run
- Location: `/root/AgentScope-Studio/database.sqlite`
- Database synchronization is enabled in development

### Quick Start Command for Future E1 Instances
```bash
# Quick setup command
cd /app && \
npm install --legacy-peer-deps && \
npm install reflect-metadata --legacy-peer-deps && \
cd packages/app && pip install -r requirements.txt && \
cd /app && npm run dev > server.log 2>&1 &
```

## Testing Protocol

### Manual Testing Checklist
- [ ] Frontend loads at http://localhost:5173
- [ ] Navigation sidebar displays all sections
- [ ] AS-Friday Copilot is accessible
- [ ] No console errors in browser
- [ ] Backend API endpoints respond (port 3000)
- [ ] Database operations work properly

### Automated Testing
- Frontend testing can be done via screenshot verification
- Backend API testing via curl commands to port 3000
- Database queries can be tested via TypeORM entities

## Integration Notes

### AgentScope Integration
To connect AgentScope applications to the studio:

```python
import agentscope

agentscope.init(
    # ...
    studio_url="http://localhost:3000"  # Backend port
)
```

### Development Environment
- Hot reload enabled for both frontend and backend
- TypeScript compilation handled by ts-node
- Vite handles frontend bundling and HMR
- SQLite provides persistent storage

## Success Indicators

**✅ Setup Complete When:**
1. Both frontend (5173) and backend (3000) are running
2. AgentScope Studio UI loads with full navigation
3. Database initializes successfully
4. No critical errors in logs
5. All required dependencies installed without conflicts

**🎯 Ready for Manual Testing:**
The application should be accessible through Emergent Preview at http://localhost:5173 with full functionality available for testing agent applications, runtime visualization, and the Friday Copilot assistant.

---
**Last Updated:** $(date)
**Environment:** Kubernetes Container with Node.js 18+ and Python 3.11+
**Status:** ✅ READY FOR PRODUCTION TESTING