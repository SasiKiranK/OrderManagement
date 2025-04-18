# # ---------- build ----------
#     FROM maven:3.9.7-eclipse-temurin-21 AS build
#     WORKDIR /app
#     COPY pom.xml mvnw ./
#     COPY .mvn .mvn
#     RUN mvn -B -q dependency:go-offline
#     COPY src src
#     RUN mvn -B -DskipTests=true package
    
#     # ---------- runtime ----------
#     FROM eclipse-temurin:21-jre
#     ENV SPRING_PROFILES_ACTIVE=prod
#     WORKDIR /app
#     COPY --from=build /app/target/user-service-*.jar app.jar
#     ENTRYPOINT ["java","-jar","/app/app.jar"]

FROM eclipse-temurin:21-jdk

# Install Maven
RUN apt-get update && apt-get install -y maven

WORKDIR /app

# Copy source code
COPY . /app

# Skip building the JAR inside Docker. We'll run Maven directly.
CMD ["mvn", "spring-boot:run"]
