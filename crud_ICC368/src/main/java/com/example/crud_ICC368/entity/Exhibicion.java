package com.example.crud_ICC368.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.HashSet;
import java.util.Set;

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

    @Setter
    @Getter
    @ManyToMany(mappedBy = "exhibiciones")
    private Set<Museo> museos = new HashSet<>();

    @Setter
    @Getter
    @ManyToMany(mappedBy = "exhibiciones")
    private Set<Artefacto> artefactos = new HashSet<>();

    public Long getId() {
        return id;
    }
}
