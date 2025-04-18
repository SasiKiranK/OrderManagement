package com.orderflow.userservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.cache.annotation.EnableCaching;


@SpringBootApplication
@EnableCaching
@EnableJpaRepositories(basePackages = "com.orderflow.userservice.repository")
public class UserServiceApplication {

  
    public static void main(String[] args) {
        SpringApplication.run(UserServiceApplication.class, args);
    }
}
