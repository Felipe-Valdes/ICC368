package com.example.crud_ICC368.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.HashSet;
import java.util.Set;

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

    @Setter
    @Getter
    @ManyToMany
    @JoinTable(
            name = "Artefacto_Exhibicion",
            joinColumns = @JoinColumn(name = "Artefactoid"),
            inverseJoinColumns = @JoinColumn(name = "Exhibicionid")
    )
    private Set<Exhibicion> exhibiciones = new HashSet<>();

    public Long getId() {
        return id;
    }
}

