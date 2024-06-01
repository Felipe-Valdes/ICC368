package com.example.crud_ICC368.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "Tematica")
public class Tematica {

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
    @ManyToMany
    @JoinTable(
            name = "Tematica_Exhbicion",
            joinColumns = @JoinColumn(name = "Tematicaid"),
            inverseJoinColumns = @JoinColumn(name = "Exhibicionid")
    )
    private Set<Exhibicion> exhibiciones = new HashSet<>();

}
