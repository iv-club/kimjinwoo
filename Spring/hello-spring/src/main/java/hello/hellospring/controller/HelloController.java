package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HelloController {

    @GetMapping("hello") //웹 어플리케이션에서 /hello를 치면 이 메서드를 매핑해줌
    public String hello(Model model) {
        model.addAttribute("data", "hello!!");
        return "hello";
    }
}
