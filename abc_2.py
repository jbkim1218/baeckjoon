import math

def calculate_velocity_components(angle, speed):
    # 각도를 라디안으로 변환
    angle_rad = math.radians(angle)
    # 수평 방향 속도 계산
    velocity_x = speed * math.cos(angle_rad)
    # 수직 방향 속도 계산
    velocity_y = speed * math.sin(angle_rad)
    return velocity_x, velocity_y

def simulate_pocketball_game(initial_angle, initial_speed, target_x, target_y, time_step=1.0):
    # 초기 속도 벡터 계산
    velocity_x, velocity_y = calculate_velocity_components(initial_angle, initial_speed)
    # 공의 초기 위치 설정 (0, 0)
    position_x, position_y = (0, 0)

    while True:
        # 공의 위치 업데이트
        position_x += velocity_x * time_step
        position_y += velocity_y * time_step

        # 공이 목표 지점에 도달했는지 확인
        if math.isclose(position_x, target_x, rel_tol=1e-2) and math.isclose(position_y, target_y, rel_tol=1e-2):
            return 'Success'

        # 공이 너무 멀리 갔는지 확인 (실패 조건)
        if position_x > 2 * target_x or position_y > 2 * target_y:
            return 'Fail'

# 사용자 입력 받기
initial_angle = float(input("초기 각도를 입력하세요 (도 단위): "))  # 초기 각도 입력
initial_speed = float(input("초기 속도를 입력하세요: "))  # 초기 속도 입력
target_x = float(input("목표 x 좌표를 입력하세요: "))  # 목표 x 좌표 입력
target_y = float(input("목표 y 좌표를 입력하세요: "))  # 목표 y 좌표 입력

# 게임 시뮬레이션 실행
result = simulate_pocketball_game(initial_angle, initial_speed, target_x, target_y)
print(result)  # 결과 출력
