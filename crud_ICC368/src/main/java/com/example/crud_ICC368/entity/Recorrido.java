package com.example.crud_ICC368.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.Date;

@Entity
@Table(name = "Recorrido")
public class Recorrido {

    @Setter
    @Getter
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Setter
    @Getter
    @Column(name = "fechaInicio")
    private Date fechaInicio;

    @Setter
    @Getter
    @Column(name = "fechaTermino")
    private Date fechaTermino;

    @Setter
    @Getter
    @ManyToOne
    @JoinColumn(name = "Exhibicionid", nullable = false)
    private Exhibicion exhibicion;

    @Setter
    @Getter
    @ManyToOne
    @JoinColumn(name = "Usuarioid", nullable = false)
    private Usuario usuario;
}
