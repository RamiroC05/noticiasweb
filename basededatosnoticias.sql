-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: proyecto_noticias
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorias` (
  `idcategorias` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`idcategorias`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (1,'Tecnología'),(2,'Deportes'),(3,'Economía'),(4,'Educación'),(5,'Arte');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `noticias`
--

DROP TABLE IF EXISTS `noticias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `noticias` (
  `idnoticias` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL,
  `descripcion` text,
  `contenido` text,
  `autor` varchar(100) DEFAULT NULL,
  `fecha_publicacion` date DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `id_cat_corresp` int DEFAULT NULL,
  PRIMARY KEY (`idnoticias`),
  KEY `relacion_idx` (`id_cat_corresp`),
  CONSTRAINT `relacion` FOREIGN KEY (`id_cat_corresp`) REFERENCES `categorias` (`idcategorias`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `noticias`
--

LOCK TABLES `noticias` WRITE;
/*!40000 ALTER TABLE `noticias` DISABLE KEYS */;
INSERT INTO `noticias` VALUES (1,'Los nuevos procesadores de 10 nucleos','procesadores mas potentes','<p>Las letras que acompa&ntilde;an a los modelos&nbsp;<strong>tienen un significado que es conveniente describir</strong>, todo sea dicho. La letra F significa que el procesador viene sin gr&aacute;<strong>F</strong>icos integrados. Es decir, necesitaremos comprar una tarjeta gr&aacute;fica s&iacute; o s&iacute;. Que no tenga letra significa que estamos ante la variante &ldquo;est&aacute;ndar&rdquo; de un modelo determinado. La letra K (unloc<strong>K</strong>ed para overclo<strong>K</strong>ing) significa que estamos ante&nbsp;<strong>la variante m&aacute;s potente de la familia y con desbloqueo total para overclocking</strong>. La letra T est&aacute; asociada a un bajo consumo y op<strong>T</strong>imizaci&oacute;n. Si tenemos la combinaci&oacute;n KF significa que estamos ante el procesador m&aacute;s ambicioso, pero sin gr&aacute;ficos integrados. La combinaci&oacute;n KA implica que estamos ante los modelos m&aacute;s potentes, en una versi&oacute;n especial&nbsp;<strong>A</strong>vengers Edition donde la caja est&aacute; &ldquo;customizada&rdquo; con la tem&aacute;tica de la saga &ldquo;Los Vengadores&rdquo;.</p>\r\n',NULL,NULL,NULL,1),(2,'Dólar: cotización de apertura hoy 1 de noviembre en Chile','Este es el comportamiento de la divisa estadounidense durante los primeros minutos de la jornada','<p>Tras la apertura el&nbsp;<strong>d&oacute;lar estadounidense</strong>&nbsp;se cotiza en el comienzo del d&iacute;a de hoy a&nbsp;<strong>942,30 pesos chilenos en promedio</strong>, de modo que supuso un cambio del 0,06% frente a los 942,90 pesos chilenos en promedio de la jornada previa.</p>\r\n\r\n<p>En relaci&oacute;n a la rentabilidad de los &uacute;ltimos siete d&iacute;as, el&nbsp;<strong>d&oacute;lar estadounidense</strong>&nbsp;acumula una bajada del&nbsp;<strong>0,95%</strong>&nbsp;aunque, por el contrario, desde hace un a&ntilde;o a&uacute;n conserva un incremento del&nbsp;<strong>18,01%</strong>. En relaci&oacute;n a d&iacute;as previos,, demostr&aacute;ndose incapaz de consolidar una clara tendencia recientemente. En referencia a la volatilidad de la &uacute;ltima semana, es visiblemente inferior a los datos conseguidos para el &uacute;ltimo a&ntilde;o (19,82%), lo que manifiesta que est&aacute; teniendo un comportamiento m&aacute;s estable de lo habitual &uacute;ltimamente.</p>\r\n',NULL,NULL,NULL,3),(3,'Cuándo juega la selección argentina en el Mundial Qatar 2022','La previa de la Copa del Mundo vibra al ritmo de la ilusión que provoca el equipo albiceleste y la organización para ver los partidos; qué hay que agendar','Este 20 de noviembre, 32 países comenzarán su participación en el Mundial Qatar 2022 con sus respectivas selecciones. Cada una con objetivos diferentes, por cuestiones lógicas de nivel y experiencia, entre muchos otros factores, pero todas con el mismo sueño: levantar la Copa del Mundo el 18 de diciembre en el Estadio Icónico de Lusail. La Argentina no es la excepción y, en esta oportunidad, buscará ganar el certamen por tercera vez en su historia luego de lo hecho en 1978 y 1986.\n',NULL,NULL,NULL,2),(4,'Feria del Libro: de la energía joven al emotivo homenaje a Almudena Grandes','En el último viernes de la edición 46 coincidieron charlas íntimas y conmovedoras con un encuentro multitudinario de adolescentes y jóvenes','En un clima cálido, íntimo y muy emotivo, con lectura de sus textos y poemas inéditos de su marido, Luis García Montero, la escritora española Almudena Grandes fue homenajeada ayer en la Feria del Libro, “un lugar que adoraba recorrer” en cada visita a Buenos Aires, como recordó la editora Paola Lucantis en la mesa que compartió con el poeta y la periodista Diana Fernández Irusta. Ante una sala colmada, con las filas de butacas completas y gente sentada en la alfombra, el tributo a la autora de Las edades de Lulú coincidió con el Encuentro Internacional de Bookfluencers, que se desarrolló durante tres horas en la sala José Hernández, también repleta de público: en este caso, adolescentes y jóvenes que siguen en YouTube y en las redes sociales a los booktubers, bookstragammers y booktokers que participaron de las sucesivas charlas.\n',NULL,NULL,NULL,5);
/*!40000 ALTER TABLE `noticias` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-08 19:59:21
