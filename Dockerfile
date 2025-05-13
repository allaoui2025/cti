# استخدم صورة Java الرسمية
FROM openjdk:17-jdk-slim

# تعريف مجلد العمل داخل الكونتينر
WORKDIR /app

# نسخ JAR من الجهاز إلى الكونتينر
COPY target/*.jar app.jar

# شنو يدير الكونتينر ملي يتشغل
ENTRYPOINT ["java", "-jar", "app.jar"]
