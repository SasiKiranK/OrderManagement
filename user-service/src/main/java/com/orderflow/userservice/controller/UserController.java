package com.orderflow.userservice.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {
    @GetMapping("/api/v1/health")
    public String healthCheck() {
        return "User Service is up!";
    }
}
