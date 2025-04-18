package com.orderflow.userservice.service.impl;

import com.orderflow.userservice.service.UserService;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.CachePut;
import org.springframework.cache.annotation.Cacheable;
import com.orderflow.userservice.dto.LoginRequest;
import com.orderflow.userservice.exception.UserNotFoundException;
import com.orderflow.userservice.model.User;
import com.orderflow.userservice.repository.UserRepository;


@Service
public class UserServiceImpl implements UserService{

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    @Autowired
    public UserServiceImpl(UserRepository userRepository,
    PasswordEncoder passwordEncoder){
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    public User createUser(User user){
        user.setPassword(passwordEncoder.encode(user.getPassword()));

        return this.userRepository.save(user);
    }

    @Override
    @Cacheable(value = "users", key = "#id")
    public User getUser(Long id){
        return userRepository.findById(id)
        .orElseThrow(() -> new UserNotFoundException(id));
    }

    @Override
    public List<User> getAllUsers(){
        return userRepository.findAll();
    }

    @Override
    @CachePut(value = "users", key = "#user.id")
    public User updateByID(User user){
        User oldUser = userRepository.findById(user.getId())
        .orElseThrow(() -> new UserNotFoundException(user.getId()));
        oldUser.setEmail(user.getEmail());
        oldUser.setName(user.getName());
        oldUser.setPassword(passwordEncoder.encode(user.getPassword()));

        return userRepository.save(oldUser);
    }

    @Override
    @CacheEvict(value = "users", key = "#id")
    public String deleteByID(Long id){
        User user = userRepository.findById(id)
        .orElseThrow(() -> new UserNotFoundException(id));

        userRepository.deleteById(id);
        return "User with ID " + id + " deleted successfully.";
    }

    @Override
    public Boolean login(LoginRequest request) {
        // User user = this.findByEmail(request.getEmail())
        // .orElseThrow(() -> new UserNotFoundException("Email not found: " + request.getEmail()));

        return true;
        // passwordEncoder.matches(request.getPassword(), user.getPassword());
    }

}
