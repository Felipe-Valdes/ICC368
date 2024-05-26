package com.example.crud_ICC368.repository;

import com.example.crud_ICC368.entity.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UsuarioRepository extends JpaRepository<Usuario, Long> {
}
