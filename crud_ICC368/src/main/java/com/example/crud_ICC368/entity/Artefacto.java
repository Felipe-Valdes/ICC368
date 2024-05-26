package com.example.crud_ICC368.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "Artefacto")
public class Artefacto {

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
    @Column(name = "descripcion")
    private String descripcion;

    @Setter
    @Getter
    @Column(name = "imagen")
    private String imagen;

    // Getters y setters
    public Long getId() {
        return id;
    }


}

