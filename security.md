# Security Policy

## Reporting Vulnerabilities

If you discover a security vulnerability, please email security@example.com

## Best Practices

- Never commit credentials or API keys
- Use environment variables for sensitive configuration
- Keep dependencies updated
- Review code before committing

## Excluded Files

The following file types are automatically excluded:
- Credential files (*.key, credentials.json)
- Backup files (*.bak, *.backup)
- Personal notes (personal_notes/)
```

**Commit message:**
```
Security: Remove sensitive files and update gitignore

- Removed test credentials and backup files
- Added comprehensive .gitignore rules
- Created SECURITY.md with best practices
- Updated README with security guidelines