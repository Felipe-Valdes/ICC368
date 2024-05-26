package com.example.crud_ICC368.controller;

import com.example.crud_ICC368.entity.Exhibicion;
import com.example.crud_ICC368.service.ExhibicionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/exhibiciones")
public class ExhibicionController {

    @Autowired
    private ExhibicionService exhibicionService;

    @GetMapping
    public List<Exhibicion> listar() {
        return exhibicionService.listarTodos();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Exhibicion> obtenerPorId(@PathVariable Long id) {
        return exhibicionService.obtenerPorId(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public Exhibicion crear(@RequestBody Exhibicion exhibicion) {
        return exhibicionService.guardar(exhibicion);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Exhibicion> actualizar(@PathVariable Long id, @RequestBody Exhibicion exhibicion) {
        if (!exhibicionService.obtenerPorId(id).isPresent()) {
            return ResponseEntity.notFound().build();
        }
        exhibicion.setId(id);
        return ResponseEntity.ok(exhibicionService.guardar(exhibicion));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminar(@PathVariable Long id) {
        if (!exhibicionService.obtenerPorId(id).isPresent()) {
            return ResponseEntity.notFound().build();
        }
        exhibicionService.eliminar(id);
        return ResponseEntity.noContent().build();
    }
}
