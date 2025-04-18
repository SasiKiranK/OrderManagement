package com.orderflow.userservice.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import com.orderflow.userservice.model.User;
import jakarta.validation.Valid; // for Spring Boot 3+
import com.orderflow.userservice.service.UserService;

@RestController
public class UserController {
    private final UserService userService;

    @GetMapping("/health")
    public String healthCheck() {
        return "User Service is up!";
    }

    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping("/createUser")
    public String createUser(@RequestBody @Valid User user) {
        return this.userService.createUser(user).toString();
        // System.out.println(user);
        // return "User Created: " + user;
    }
}