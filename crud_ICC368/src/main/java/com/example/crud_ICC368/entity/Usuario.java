package com.example.crud_ICC368.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "Usuario")
public class Usuario {

    @Setter
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Setter
    @Getter
    @Column(name = "nombre")
    private String nombre;

    @Setter
    @Getter
    @Column(name = "apellidos")
    private String apellidos;

    @Setter
    @Getter
    @Column(name = "correo")
    private String correo;

    @Setter
    @Getter
    @Column(name = "clave")
    private String clave;

    @Setter
    @Getter
    @Column(name = "rol")
    private String rol;

    // Constructor, getters y setters
    public Long getId() {
        return id;
    }
}
