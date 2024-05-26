package com.example.crud_ICC368.service;

import com.example.crud_ICC368.entity.Exhibicion;
import com.example.crud_ICC368.repository.ExhibicionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ExhibicionService {

    @Autowired
    private ExhibicionRepository exhibicionRepository;

    public List<Exhibicion> listarTodos() {
        return exhibicionRepository.findAll();
    }

    public Optional<Exhibicion> obtenerPorId(Long id) {
        return exhibicionRepository.findById(id);
    }

    public Exhibicion guardar(Exhibicion exhibicion) {
        return exhibicionRepository.save(exhibicion);
    }

    public void eliminar(Long id) {
        exhibicionRepository.deleteById(id);
    }
}
