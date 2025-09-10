# Bible Study Forum Design

## Overview
This document outlines a concept for an online forum where Christians can gather for Bible study. Users log in with their Google Gmail account, share notes, and interact with pastors who can post study guides and questions.

## Authentication
- Use Google Sign-In (OAuth 2.0) to allow users to authenticate with Gmail.
- Store minimal profile data: name, email, and avatar.
- Secure endpoints with session cookies or JWTs.

## User Roles
- **Member**: posts notes, comments, and uploads study materials.
- **Pastor/Moderator**: creates discussion series, posts prepared questions and notes, and manages content.

## Core Features
1. **Series and Threads**
   - Organize discussions by series (e.g., "Study on Romans").
   - Each series contains threads for individual lessons or passages.

2. **Notes and Attachments**
   - Support rich-text notes, images, and PDF attachments.
   - Pastor can upload prepared questions or slides.

3. **Bible Passage Integration**
   - Use the existing `bible` CLI to fetch passages for insertion into posts.
   - Optionally expose a web API wrapper around the CLI for dynamic verse lookup.

4. **Notifications**
   - Email or in-app alerts when a pastor posts new material or when someone replies.

5. **Search and Tags**
   - Tag threads by book or topic (e.g., "Romans", "Faith").
   - Provide search across titles and notes.

## Technology Stack
- **Backend**: Python (Django or Flask) with RESTful API endpoints.
- **Frontend**: React or server-rendered templates.
- **Database**: PostgreSQL for persistent storage of users, threads, and notes.
- **Authentication**: `google-auth` / `oauthlib` for OAuth flow.
- **File Storage**: Local or cloud storage (e.g., AWS S3) for attachments.

## Future Enhancements
- Mobile-friendly interface or dedicated mobile app.
- Live group chat or video integration for real-time Bible study.
- Role-based access for private groups or leadership teams.

