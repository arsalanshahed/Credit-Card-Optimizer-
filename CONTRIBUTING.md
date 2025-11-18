# Contributing to Credit Card Optimizer

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/Credit-Card-Optimizer-.git
   cd credit-card-optimizer
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Development Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Docker (Unified)
```bash
docker compose up --build
```

## 🔄 Making Changes

1. **Make your changes** in your feature branch
2. **Test thoroughly** - ensure all functionality works
3. **Update documentation** if needed
4. **Commit your changes**:
   ```bash
   git commit -m "Add: Description of your changes"
   ```
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request** on GitHub

## 📋 Pull Request Guidelines

- **Clear title** describing the change
- **Detailed description** of what was changed and why
- **Screenshots** for UI changes (if applicable)
- **Test results** showing the changes work
- **Reference issues** if fixing a bug

## 🎯 Areas for Contribution

- **New Features**: Additional credit cards, new categories, advanced analytics
- **UI/UX Improvements**: Better designs, animations, accessibility
- **Performance**: Optimizations, caching, faster load times
- **Documentation**: Better docs, examples, tutorials
- **Testing**: Unit tests, integration tests, E2E tests
- **Bug Fixes**: Fixing issues and improving stability

## 📊 Code Style

### Python (Backend)
- Follow PEP 8 style guide
- Use type hints where possible
- Add docstrings to functions
- Keep functions focused and small

### TypeScript (Frontend)
- Use TypeScript strict mode
- Follow React best practices
- Use functional components with hooks
- Keep components small and reusable

## ✅ Testing

Before submitting a PR, ensure:
- [ ] All existing tests pass
- [ ] New features have tests (if applicable)
- [ ] Code runs locally without errors
- [ ] Docker build succeeds
- [ ] No console errors or warnings

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Your contributions make this project better for everyone. Thank you for taking the time to contribute!

