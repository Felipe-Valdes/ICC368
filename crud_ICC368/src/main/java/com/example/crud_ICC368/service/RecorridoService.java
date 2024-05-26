package com.example.crud_ICC368.service;

import com.example.crud_ICC368.entity.Recorrido;
import com.example.crud_ICC368.repository.RecorridoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class RecorridoService {

    @Autowired
    private RecorridoRepository recorridoRepository;

    public List<Recorrido> listarTodos() {
        return recorridoRepository.findAll();
    }

    public Optional<Recorrido> obtenerPorId(Long id) {
        return recorridoRepository.findById(id);
    }

    public Recorrido guardar(Recorrido recorrido) {
        return recorridoRepository.save(recorrido);
    }

    public void eliminar(Long id) {
        recorridoRepository.deleteById(id);
    }
}
