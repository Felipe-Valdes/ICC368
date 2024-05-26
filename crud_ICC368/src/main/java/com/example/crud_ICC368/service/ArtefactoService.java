package com.example.crud_ICC368.service;

import com.example.crud_ICC368.entity.Artefacto;
import com.example.crud_ICC368.repository.ArtefactoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ArtefactoService {
    @Autowired
    private ArtefactoRepository artefactoRepository;

    public List<Artefacto> listarTodos() {
        return artefactoRepository.findAll();
    }

    public Optional<Artefacto> obtenerPorId(Long id) {
        return artefactoRepository.findById(id);
    }

    public Artefacto guardar(Artefacto artefacto) {
        return artefactoRepository.save(artefacto);
    }

    public void eliminar(Long id) {
        artefactoRepository.deleteById(id);
    }
}
