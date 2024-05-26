package com.example.crud_ICC368.service;

import com.example.crud_ICC368.entity.Museo;
import com.example.crud_ICC368.repository.MuseoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class MuseoService {
    @Autowired
    private MuseoRepository museoRepository;

    public List<Museo> listarTodos() {
        return museoRepository.findAll();
    }

    public Optional<Museo> obtenerPorId(Long id) {
        return museoRepository.findById(id);
    }

    public Museo guardar(Museo museo) {
        return museoRepository.save(museo);
    }

    public void eliminar(Long id) {
        museoRepository.deleteById(id);
    }
}
