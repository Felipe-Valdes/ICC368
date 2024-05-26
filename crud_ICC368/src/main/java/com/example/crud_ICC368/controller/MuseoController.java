package com.example.crud_ICC368.controller;

import com.example.crud_ICC368.entity.Museo;
import com.example.crud_ICC368.service.MuseoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/museos")
public class MuseoController {

    @Autowired
    private MuseoService museoService;

    @GetMapping
    public List<Museo> listar() {
        return museoService.listarTodos();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Museo> obtenerPorId(@PathVariable Long id) {
        return museoService.obtenerPorId(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public Museo crear(@RequestBody Museo museo) {
        return museoService.guardar(museo);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Museo> actualizar(@PathVariable Long id, @RequestBody Museo museo) {
        if (!museoService.obtenerPorId(id).isPresent()) {
            return ResponseEntity.notFound().build();
        }
        museo.setId(id);
        return ResponseEntity.ok(museoService.guardar(museo));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminar(@PathVariable Long id) {
        if (!museoService.obtenerPorId(id).isPresent()) {
            return ResponseEntity.notFound().build();
        }
        museoService.eliminar(id);
        return ResponseEntity.noContent().build();
    }
}
