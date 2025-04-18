package com.orderflow.userservice.service.Impl;

import com.orderflow.userservice.service.UserService;

import org.springframework.stereotype.Service;

import com.orderflow.userservice.model.User;

@Service
public class UserServiceImpl implements UserService{

    @Override
    public User createUser(User user){
        return user;
    }
    
}
