# 🤖 AI-Powered Attendance System

<p align="center">
  <b>AI-powered dual-modality biometric attendance system using Face Recognition and Voice Verification.</b>
</p>

<p align="center">
  <a href="https://smartclass-three.vercel.app/">🌐 Live Demo</a>
  •
  <a href="https://github.com/Sanskriti199/SmartClass-Frontend">🎨 Frontend Repository</a>
</p>

---

## 🌐 Live Demo

🔗 **Live Application:** https://smartclass-three.vercel.app/

🎨 **Frontend Repository:** https://github.com/Sanskriti199/SmartClass-Frontend

> The deployed interface is the Streamlit-based frontend of the SmartClass AI Attendance System.

---

# 🚀 Deployment

The AI Attendance System is deployed using **Streamlit Cloud and Vercel**, providing a publicly accessible web interface while supporting the application's backend services.

- ☁️ **Streamlit** — Deployment of the Streamlit application
- ▲ **Vercel** — Deployment of the web frontend
- 🗄️ **Supabase** — Cloud database and real-time data management

---

## 📌 About The Project

The **AI-Powered Attendance System** is a secure and intelligent attendance management platform that combines **facial recognition and voice verification** for biometric authentication.

The system is designed to reduce **proxy attendance**, automate attendance management, and improve authentication reliability through a **dual-modality biometric verification approach**.

The application consists of an interactive **Streamlit frontend**, a **Flask REST API backend**, dedicated face and voice processing pipelines, and **Supabase** integration for real-time attendance and student data management.

---

## ✨ Key Features

- 👤 **Face Recognition**
  - Detects and recognizes registered students.
  - Uses OpenCV, dlib, and face recognition models.

- 🎙️ **Voice Verification**
  - Verifies students using their voice.
  - Uses Resemblyzer and Librosa for speaker verification and audio processing.

- 🔐 **Dual-Modality Authentication**
  - Combines facial and voice verification.
  - Provides an additional layer of identity validation.

- 📋 **Automated Attendance**
  - Automatically records attendance after successful authentication.
  - Reduces manual attendance errors and proxy attendance.

- 👨‍🎓 **Student Enrollment**
  - Register students and their biometric information.
  - Supports face and voice enrollment.

- 👨‍🏫 **Teacher Dashboard**
  - Create and manage subjects.
  - Manage students and attendance records.

- 🗄️ **Supabase Integration**
  - Stores student, subject, and attendance-related data.
  - Provides cloud-based database management.

- 🎨 **Interactive Streamlit UI**
  - User-friendly interface for students and teachers.
  - Designed for smooth attendance workflows.

- 🔗 **Flask REST API**
  - Provides backend services through REST APIs.
  - Handles communication between the application and backend services.

---

# 🛠️ Tech Stack

## 🎨 Frontend

- **Streamlit**
- HTML
- CSS
- Python-based UI components

## ⚙️ Backend

- **Python**
- **Flask**
- REST API

## 👁️ Computer Vision & Face Recognition

- **OpenCV**
- **dlib**
- **face_recognition**
- **face_recognition_models**
- **Pillow**

## 🎙️ Voice & Audio Processing

- **Resemblyzer**
- **Librosa**

## 🧠 Machine Learning & Data Processing

- **Scikit-learn**
- **NumPy**
- **Pandas**

## 🗄️ Database

- **Supabase**

## 🔐 Security & Utilities

- **bcrypt**
- **Segno**
- **Setuptools**

---

# 📦 Main Dependencies

The project primarily depends on the following libraries:

| Dependency | Purpose |
|------------|---------|
| `streamlit` | Interactive application interface |
| `flask` | REST API backend |
| `opencv-python` | Image processing and computer vision |
| `dlib-bin` | Facial landmark and face processing |
| `face_recognition` | Face detection and face recognition |
| `face_recognition_models` | Pre-trained face recognition models |
| `resemblyzer` | Speaker embedding and voice verification |
| `librosa` | Audio processing and feature extraction |
| `scikit-learn` | Machine learning utilities |
| `numpy` | Numerical computation |
| `pandas` | Data manipulation and processing |
| `supabase` | Cloud database integration |
| `bcrypt` | Password hashing and authentication security |
| `pillow` | Image processing |
| `segno` | QR code generation |
| `setuptools` | Python package management |

---

# 🏗️ System Architecture

```text
                         ┌───────────────────────┐
                         │      Streamlit UI     │
                         │   Student / Teacher   │
                         └───────────┬───────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    │                                 │
          ┌─────────▼──────────┐            ┌─────────▼──────────┐
          │ Face Recognition   │            │ Voice Verification │
          │     Pipeline       │            │      Pipeline      │
          │                    │            │                    │
          │ OpenCV             │            │ Librosa            │
          │ dlib               │            │ Resemblyzer        │
          │ face_recognition   │            │ Speaker Embeddings │
          └─────────┬──────────┘            └─────────┬──────────┘
                    │                                 │
                    └────────────────┬────────────────┘
                                     │
                            ┌────────▼────────┐
                            │   Flask REST API│
                            │     Backend     │
                            └────────┬────────┘
                                     │
                            ┌────────▼────────┐
                            │    Supabase     │
                            │     Database    │
                            └─────────────────┘
