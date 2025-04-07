# استخدام صورة Python الأساسية
FROM python:3.9

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ وتثبيت المتطلبات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# فتح المنفذ 5000 لتطبيق Flask
EXPOSE 5000

# تشغيل التطبيق عند بدء الحاوية
CMD ["python", "app.py"]
