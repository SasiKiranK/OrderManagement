package com.orderflow.userservice.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.orderflow.userservice.model.User;

public interface UserRepository extends JpaRepository<User, Long> {
    
}
