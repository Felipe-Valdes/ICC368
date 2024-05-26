package com.example.crud_ICC368.controller;

import com.example.crud_ICC368.entity.Recorrido;
import com.example.crud_ICC368.service.RecorridoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/recorridos")
public class RecorridoController {

    @Autowired
    private RecorridoService recorridoService;

    @GetMapping
    public List<Recorrido> listar() {
        return recorridoService.listarTodos();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Recorrido> obtenerPorId(@PathVariable Long id) {
        return recorridoService.obtenerPorId(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public Recorrido crear(@RequestBody Recorrido recorrido) {
        return recorridoService.guardar(recorrido);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Recorrido> actualizar(@PathVariable Long id, @RequestBody Recorrido recorrido) {
        if (!recorridoService.obtenerPorId(id).isPresent()) {
            return ResponseEntity.notFound().build();
        }
        recorrido.setId(id);
        return ResponseEntity.ok(recorridoService.guardar(recorrido));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminar(@PathVariable Long id) {
        if (!recorridoService.obtenerPorId(id).isPresent()) {
            return ResponseEntity.notFound().build();
        }
        recorridoService.eliminar(id);
        return ResponseEntity.noContent().build();
    }
}
