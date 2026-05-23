# ==========================================
# STAGE 1: Build & Verification Environment
# ==========================================
FROM alpine:3.19 AS builder

WORKDIR /app

# Copy website assets into the build context
COPY index.html style.css script.js ./
COPY images/ ./images/

# Verification step to ensure files exist before final packaging
RUN test -f index.html && test -f style.css && test -f script.js

# ==========================================
# STAGE 2: Ultra-lightweight Production Image
# ==========================================
FROM nginx:1.25-alpine-slim

# Copy custom Nginx optimization settings if you have them, 
# otherwise use default or copy straight to the web root
COPY --from=builder /app /usr/share/nginx/html

# Expose port 80 to the Cloud66 internal routing fabric
EXPOSE 80

# Run Nginx in the foreground so the container stays active
CMD ["nginx", "-g", "daemon off;"]