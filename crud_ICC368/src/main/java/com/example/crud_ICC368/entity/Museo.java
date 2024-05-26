package com.example.crud_ICC368.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "Museo")
public class Museo {

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
    @Column(name = "ubicacion")
    private String ubicacion;

    @Setter
    @Getter
    @ManyToMany
    @JoinTable(
            name = "Museo_Exhibicion",
            joinColumns = @JoinColumn(name = "Museoid"),
            inverseJoinColumns = @JoinColumn(name = "Exhibicionid")
    )
    private Set<Exhibicion> exhibiciones = new HashSet<>();

    public Long getId() {
        return id;
    }
}
