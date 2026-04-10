import cv2
from modules.deteccao import DetectorBagagem

def main():
    cap = cv2.VideoCapture(0) # 0 para webcam
    detector = DetectorBagagem()

    print("Sistema de Monitoramento de Bagagens - ELE634 Iniciado.")
    print("Pressione 'q' para sair.")

    while cap.isOpened():
        success, frame = cap.read()
        if not success: break

        # Chama o módulo de detecção
        resultado = detector.detectar(frame)
        
        # Desenha os resultados no frame
        annotated_frame = resultado.plot()

        cv2.imshow("Monitoramento Ejetora (S2)", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()