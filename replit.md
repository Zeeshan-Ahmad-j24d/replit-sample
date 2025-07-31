# Flask Multi-Environment Application

## Overview

This is a Flask web application designed with a robust multi-environment configuration system. The application demonstrates best practices for managing different deployment environments (development and production) with automatic configuration switching based on environment variables.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Configuration Management**: Environment-based configuration system using Python modules
- **Entry Point**: `main.py` serves as the application launcher
- **Core Application**: `app.py` contains route definitions and Flask app initialization

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default templating engine)
- **UI Framework**: Bootstrap with dark theme
- **Icons**: Feather Icons for consistent iconography
- **Responsive Design**: Mobile-first responsive layout

## Key Components

### Configuration System
- **Environment Detection**: Uses `FLASK_ENV` environment variable to determine runtime environment
- **Modular Config**: Separate configuration files for development and production environments
- **Default Fallback**: Defaults to development configuration if environment is not specified

### Core Routes
- **Home Route** (`/`): Main landing page displaying environment information
- **About Route** (`/about`): Information about the application
- **Health Check** (`/health`): JSON endpoint for monitoring application status
- **Config Display** (`/config`): JSON endpoint showing current configuration

### Environment Configurations
- **Development**: Debug mode enabled, runs on port 5000
- **Production**: Debug mode disabled, runs on port 5005

## Data Flow

1. **Application Startup**: `main.py` imports the Flask app and configuration
2. **Environment Detection**: `config/__init__.py` checks `FLASK_ENV` environment variable
3. **Configuration Loading**: Appropriate environment config (development/production) is imported
4. **Route Handling**: Flask routes serve templates with environment-specific data
5. **Template Rendering**: Jinja2 templates receive environment variables for dynamic display

## External Dependencies

### Python Packages
- **Flask**: Core web framework for handling HTTP requests and responses
- **Jinja2**: Template engine (included with Flask)

### Frontend Dependencies (CDN)
- **Bootstrap**: CSS framework for responsive design and components
- **Feather Icons**: Icon library for consistent UI elements

### Environment Variables
- **FLASK_ENV**: Controls which environment configuration to load (`development` or `production`)
- **SESSION_SECRET**: Flask session secret key (defaults to development key if not set)

## Deployment Strategy

### Environment Management
- **Development**: Intended for local development with debug mode and verbose logging
- **Production**: Optimized for live deployment with security features enabled

### Port Strategy
- **Development**: Port 5000 (Flask default)
- **Production**: Port 5005 (avoiding conflicts with development instances)

### Security Considerations
- Session secret key should be set via environment variable in production
- Debug mode automatically disabled in production environment
- Error handling with custom 404 page (partially implemented)

### Monitoring
- Health check endpoint (`/health`) provides JSON status for monitoring tools
- Configuration endpoint (`/config`) allows runtime configuration inspection
- Environment information displayed in UI for transparency

The application follows a clean separation of concerns with environment-specific configurations, making it easy to deploy across different environments while maintaining consistency and security best practices.