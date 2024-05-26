package com.example.crud_ICC368.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

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

    public long getId() {
        return id;
    }


}
