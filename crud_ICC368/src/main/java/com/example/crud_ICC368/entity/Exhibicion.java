package com.example.crud_ICC368.entity;


import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "Exhibicion")
public class Exhibicion {

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

    // Getters y setters
    public Long getId() {
        return id;
    }


}
