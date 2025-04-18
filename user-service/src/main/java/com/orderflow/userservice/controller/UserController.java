package com.orderflow.userservice.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.orderflow.userservice.dto.LoginRequest;
import com.orderflow.userservice.model.User;
import jakarta.validation.Valid;
import com.orderflow.userservice.service.UserService;

@RestController
@RequestMapping("/api/v1/users")
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

    @PostMapping("/create")
    public String createUser(@RequestBody @Valid User user) {
        return this.userService.createUser(user).toString();
    }

    @GetMapping("/{id}")
        public ResponseEntity<User> getUser(@PathVariable Long id) {
    return ResponseEntity.ok(this.userService.getUser(id));
    }

    @GetMapping("/getAll")
    public ResponseEntity<List<User>> getAllUsers() {
        return ResponseEntity.ok(this.userService.getAllUsers());
    }

    @PutMapping("/update/{id}")
    public ResponseEntity<User> updateByID(@RequestBody User user) {
        return ResponseEntity.ok(this.userService.updateByID(user));
    }

    @DeleteMapping("/delete/{id}")
    public ResponseEntity<String> deleteByID(@PathVariable Long id) {
        return ResponseEntity.ok(this.userService.deleteByID(id));
    }

    @PostMapping("/login")
    public ResponseEntity<Boolean> login(@RequestBody @Valid LoginRequest login) {
        return ResponseEntity.ok(this.userService.login(login));
    }
}