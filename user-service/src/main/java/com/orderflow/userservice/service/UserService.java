package com.orderflow.userservice.service;

import java.util.List;

import com.orderflow.userservice.dto.LoginRequest;
import com.orderflow.userservice.model.User;

import jakarta.validation.Valid;


public interface UserService {
    User createUser(User user);

    User getUser(Long id);

    List<User> getAllUsers();

    User updateByID(User user);

    String deleteByID(Long id);

    Boolean login(LoginRequest login);
    
}